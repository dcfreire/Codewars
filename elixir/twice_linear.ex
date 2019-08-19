defmodule Twice do

    def dbl_linear(n) do
     y = fn x -> 2*x+1 end
     z = fn x -> 3*x+1 end
     n_op = trunc(:math.log2(n))
     Enum.map(1..n_op + 2, fn k ->
      Enum.map(0..trunc(:math.pow(2, k) - 1),fn x ->
      dig = Integer.digits(x, 2)
      Enum.concat(List.duplicate(0, k - Enum.count(dig)), dig)
      |>Enum.reduce(1, fn l, acc ->
       cond do
        l == 1 ->
         z.(acc)
        true ->
         y.(acc)
       end
      end)
      end
      )end)
      |> Enum.concat()
      |> Enum.uniq()
      |> Enum.sort()
      |> List.insert_at(0, 1)
      |> Enum.at(n)
     end
end
