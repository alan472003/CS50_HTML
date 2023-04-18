main = do
  putStrLn "Enter a temperature in Fahrenheit:"
  input <- getLine
  let fahrenheit = read input :: Float
  let celsius = (fahrenheit - 32) * 5 / 9
  putStrLn ("The temperature in Celsius is " ++ show celsius)