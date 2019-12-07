fuelRequired :: Integer -> Integer
fuelRequired m | m < 9 = 0
fuelRequired m = (\r -> r + fuelRequired r) (floor (fromIntegral m / 3) - 2)

main = interact (flip (++) "\n" . show . sum . map (fuelRequired . read) . lines)
