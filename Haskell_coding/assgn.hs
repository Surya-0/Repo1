import Data.Typeable (typeOf)

-- Questions 1 and 2
-- mod' :: Double -> Double -> Double
-- mod' a b = a - fromIntegral (floor (a / b) * floor b)

main :: IO ()
main = do
    putStrLn "My address is 123 ABC, 2nd street Royal Land"
    putStrLn "Enter the first number: "
    input1 <- getLine
    putStrLn "Enter the second number: "
    input2 <- getLine
    putStrLn $ "Numbers entered: " ++ show input1 ++ " " ++ show input2
    putStrLn $ "Type of input1: " ++ show (typeOf input1)
    let num1 = read input1 :: Double
    let num2 = read input2 :: Double
    let sum = num1 + num2
    let diff = num1 - num2
    let product = num1 * num2
    let division = num1 / num2
    let remainderResult = mod' num1 num2
    putStrLn $ "The sum is: " ++ show sum
    putStrLn $ "The difference is: " ++ show diff
    putStrLn $ "The product is: " ++ show product
    putStrLn $ "The quotient is: " ++ show division
    putStrLn $ "The remainder is: " ++ show remainderResult

Questions 3,4,5

-- main :: IO ()
-- main = do
--     putStrLn "Enter the value in kilo meters"
--     input1 <- getLine
--     putStrLn "Enter the value in Fahrenheit"
--     input2 <- getLine
--     putStrLn "Enter the value in feet"
--     input3 <- getLine
--     let num1 = read input1 :: Double
--     let num2 = read input2 :: Double
--     let num3 = read input3 :: Double
--     let celsius = (5 / 9) * (num2 - 32.0)
--     putStrLn ("The value in m : "++show(num1*1000.0))
--     putStrLn ("The value in m : "++show(celsius))
--     putStrLn ("The value in cm : "++show(num3 * 30.0))


-- Questions 6,7,8

-- main :: IO ()
-- main = do
--     putStrLn "Enter a number for calculation"
--     input1 <- getLine
--     putStrLn "Enter the principal value"
--     input2 <- getLine
--     putStrLn "Enter the rate of interest"
--     input3 <- getLine
--     putStrLn "Enter the time period"
--     input4 <- getLine
--     let num1 = read input1 :: Double -- type conversion to double
--     let num2 = read input2 :: Double -- type conversion to double
--     let num3 = read input3 :: Double
--     let num4 = read input4 :: Double
--     let square = num1 ^ 2
--     let cube = num1 ^ 3
--     let square_root = sqrt num1
--     let simple_interest = (num2*num3*num4)/100.0
--     let compoundInterest = num2 * (1 + num3) ** (num4) - num2
--     putStrLn $ "Square of the number: " ++ show square
--     putStrLn $ "Cube of the number: " ++ show cube
--     putStrLn $ "Square root of the number: " ++ show square_root
--     putStrLn $ "Simple Interest: " ++ show simple_interest
--     putStrLn $ "Compound Interest: " ++ show compoundInterest

-- Questions 9,10

main :: IO ()
main = do
    