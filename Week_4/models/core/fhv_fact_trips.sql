{{
    config(
        materialized='table'
    )
}}

with fhv_tripdata as (
    select *, 
        'Green' as service_type
    from {{ ref('stg_fhv_tripdata') }}
), 


dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)
select fhv_tripdata.*, 
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone, 

from fhv_tripdata
inner join dim_zones as pickup_zone
on fhv_tripdata.PUlocationID = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on fhv_tripdata.DOlocationID = dropoff_zone.locationid