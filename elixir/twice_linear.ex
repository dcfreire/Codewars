defmodule Twice do

    def dbl_linear(n) do
     y = fn x -> 2*x+1 end
     z = fn x -> 3*x+1 end
     Enum.reduce(1..n, {[1], 0, 0}, fn _, acc ->
       yaux = y.(Enum.at(elem(acc, 0), elem(acc, 1)))
       zaux = z.(Enum.at(elem(acc, 0), elem(acc, 2)))
       cond do
        yaux <= zaux ->
         acc = {elem(acc, 0) ++ [yaux], elem(acc, 1) + 1, elem(acc, 2)}
         if yaux == zaux do
         {elem(acc, 0), elem(acc, 1), elem(acc, 2) + 1}
        else
         acc
        end
        true ->
         {elem(acc, 0) ++ [zaux], elem(acc, 1), elem(acc, 2) + 1}
       end
     end)
     |> elem(0)
     |> List.last()
     end
end
