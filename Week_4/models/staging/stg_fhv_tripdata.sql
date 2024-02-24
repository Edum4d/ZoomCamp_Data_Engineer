{{ config(materialized='view') }}

with renamed as (

    select * from {{ source('staging', 'fhv_tripdata') }}

)



SELECT
    dispatching_base_num,
    PARSE_TIMESTAMP("%Y-%m-%d %k:%M:%S", pickup_datetime) AS pickup_datetime,
    PARSE_TIMESTAMP("%Y-%m-%d %k:%M:%S", dropoff_datetime) AS dropoff_datetime,
    pulocationid,
    dolocationid,
    sr_flag,
    affiliated_base_number
FROM renamed
WHERE EXTRACT(YEAR FROM PARSE_TIMESTAMP("%Y-%m-%d %k:%M:%S", pickup_datetime)) = 2019