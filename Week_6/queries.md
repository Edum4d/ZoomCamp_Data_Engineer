CREATE MATERIALIZED VIEW trip_time_statistics2 AS
SELECT
    tz1.zone AS pickup_zone,
    tz2.zone AS dropoff_zone,
    AVG(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS average_trip_time,
    MIN(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS min_trip_time,
    MAX(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS max_trip_time
FROM
    trip_data td
JOIN
    taxi_zone tz1 ON td.pulocationid = tz1.location_id
JOIN
    taxi_zone tz2 ON td.dolocationid = tz2.location_id
GROUP BY
    tz1.zone, tz2.zone;


SELECT
    pickup_zone,
    dropoff_zone,
    average_trip_time
FROM
    trip_time_statistics2
ORDER BY
    average_trip_time DESC
LIMIT 5;

SELECT
    pickup_zone,
    dropoff_zone,
    average_trip_time,
    trip_count
FROM (
    SELECT
        pickup_zone,
        dropoff_zone,
        average_trip_time,
        COUNT(*) AS trip_count,
        RANK() OVER (ORDER BY average_trip_time DESC) AS rank
    FROM
        trip_time_statistics
    GROUP BY
        pickup_zone,
        dropoff_zone,
        average_trip_time
) AS ranked_trips
WHERE
    rank = 1;



WITH LatestPickup AS (
    SELECT MAX(tpep_pickup_datetime) AS latest_pickup_time
    FROM trip_data
),
FilteredPickups AS (
    SELECT
        pulocationid,
        COUNT(*) AS pickup_count
    FROM
        trip_data
    WHERE
        tpep_pickup_datetime >= (SELECT latest_pickup_time - interval '17 hours' FROM LatestPickup)
    GROUP BY
        pulocationid
)


SELECT
    tz.zone AS pickup_zone,
    fp.pickup_count
FROM
    FilteredPickups fp
JOIN
    taxi_zone tz ON fp.pulocationid = tz.location_id
ORDER BY
    fp.pickup_count DESC
LIMIT 3;