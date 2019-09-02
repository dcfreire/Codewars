defmodule Twice do
  def dbl_linear(n) do
    y = fn x -> 2 * x + 1 end
    z = fn x -> 3 * x + 1 end

    Enum.reduce(1..n, {%{0 => 1}, 0, 0}, fn x, acc ->
      yaux = y.(Enum.at(elem(acc, 0), length(elem(acc, 0)) - elem(acc, 1)-1))
      zaux = z.(Enum.at(elem(acc, 0), length(elem(acc, 0)) - elem(acc, 2)-1))

      cond do
        yaux <= zaux ->
          acc = {Map.put(elem(acc, 0), x, yaux), elem(acc, 1) + 1, elem(acc, 2)}

          if yaux == zaux do
            {elem(acc, 0), elem(acc, 1), elem(acc, 2) + 1}
          else
            acc
          end

        true ->
          {Map.put(elem(acc,0), x, zaux), elem(acc, 1), elem(acc, 2) + 1}
      end
    end)
    |> elem(0)
    |> Map.get(n)
  end
end
