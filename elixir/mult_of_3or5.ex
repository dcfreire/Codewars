defmodule Challenge do
  def solution(number) do
   Enum.filter(1..number-1, fn x -> rem(x, 3) == 0 or rem(x, 5) == 0 end)
   |> Enum.sum()
  end
end

solution(10)
