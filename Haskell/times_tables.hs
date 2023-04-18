module Main where

main :: IO ()
main = do
  mapM_ putStrLn [show x ++ " * " ++ show y ++ " = " ++ show (x * y) | x <- [1..12], y <- [1..12]]