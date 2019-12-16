fuelRequired :: Integer -> Integer
fuelRequired m = floor (fromIntegral m / 3) - 2

main = interact (flip (++) "\n" . show . sum . map (fuelRequired . read) . lines)
