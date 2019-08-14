defmodule Twice do

    def dbl_linear(n) do
     y = fn x -> 2*x+1 end
     z = fn x -> 3*x+1 end
     final = Enum.reduce(1..n-1, "0",fn x, acc->
       cond do
        String.match?(acc, ~r/^(1)\1*$/) ->
         "0" <> String.replace(acc, "1", "0")
         String.match?(acc, ~r/10/) ->
           String.replace(acc, "10", "01", global: false)
         true ->
          String.replace_prefix(acc, "0", "1")
       end
      end
      )
      |>String.to_charlist()
      |>Enum.reduce(1, fn x, acc ->
        cond do
         x == 49 ->
          IO.puts("3x+1")

          IO.inspect(acc)
          z.(acc)
         true ->
          IO.puts("2x+1")
          IO.inspect(acc)
          y.(acc)
        end
       end
       )
      cond do
       n == 0 ->
        1
       n == 1 ->
        3
       n == 2 ->
        4
       true ->
        final
      end
     end
end
