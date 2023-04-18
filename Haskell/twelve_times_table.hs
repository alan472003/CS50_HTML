module Main where

main :: IO ()
main = do
  mapM_ putStrLn [show x ++ " * 12 = " ++ show (x * 12) | x <- [1..12]]