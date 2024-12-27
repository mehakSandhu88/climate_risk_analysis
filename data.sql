-- Create table for climate data
CREATE TABLE ClimateData (
    Year INT,
    Temperature FLOAT,
    Precipitation FLOAT,
    RiskScore FLOAT
);

-- Insert sample data (replace these values with actual data)
INSERT INTO ClimateData (Year, Temperature, Precipitation, RiskScore) VALUES
(2000, 15.3, 120.5, 78.2),
(2001, 16.1, 110.3, 80.1),
(2002, 14.8, 130.6, 77.9);

-- Query to get basic statistics
SELECT 
    AVG(Temperature) AS AvgTemp,
    MIN(Temperature) AS MinTemp,
    MAX(Temperature) AS MaxTemp,
    AVG(Precipitation) AS AvgPrecip,
    MIN(Precipitation) AS MinPrecip,
    MAX(Precipitation) AS MaxPrecip
FROM ClimateData;

-- Query for anomalies (e.g., temperature > 30)
SELECT * FROM ClimateData
WHERE Temperature > 30;

-- Export data to CSV for further analysis
-- Use your database tool or script to export this query result
SELECT * FROM ClimateData;
