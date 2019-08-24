defmodule OddRow do
  def odd_row(n) do
    Enum.map((div(n * (n + 1), 2) - n + 1)..div(n * (n + 1), 2), fn x -> 2 * x - 1 end)
  end
end
