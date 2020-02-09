defmodule Factorial do
  def of(0), do: 1
  def of(n) when n > 0, do: n * of(n - 1)
end

defmodule Dec2Fact do
  def dec_2_fact_string(n) do
    Enum.reduce_while(1..(n * n * n), {[], n}, fn x, acc ->
      cond do
        elem(acc, 1) == 0 ->
          {:halt, acc}

        true ->
          {:cont, {[rem(elem(acc, 1), x) | elem(acc, 0)], div(elem(acc, 1), x)}}
      end
    end)
    |> elem(0)
    |> Enum.map(fn x -> Integer.to_string(x, 36) end)
    |> List.to_string()
  end

  def fact_string_2_dec(str) do
    str
    |> String.graphemes()
    |> Enum.map(fn x -> String.to_integer(x, 36) end)
    |> (&Enum.reduce(&1, {0, length(&1) - 1}, fn x, acc ->
          {elem(acc, 0) + Factorial.of(elem(acc, 1)) * x, elem(acc, 1) - 1}
        end)).()
    |> elem(0)
  end
end
