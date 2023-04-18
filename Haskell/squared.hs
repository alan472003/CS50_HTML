main = do
  putStrLn "Enter a number:"
  input <- getLine
  let number = read input :: Float
  let squared = number * number
  putStrLn ("The square of " ++ show number ++ " is " ++ show squared)