-- Column names must be: band_name and lifespan (in years)
-- Get bands and order by longevity

SELECT band_name, COALESCE(split, YEAR(CURDATE())) - formed AS lifespan FROM metal_bands
WHERE style LIKE "%Glam Rock%"
ORDER BY lifespan DESC
