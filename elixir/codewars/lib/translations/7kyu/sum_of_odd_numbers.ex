defmodule SumOfOdd do
  def row_sum_odd_numbers(n) do
    Enum.map(div((n*(n+1)),2) - n + 1..div(n*(n+1),2), fn x -> 2*x - 1 end)
    |> Enum.sum()
  end
end
