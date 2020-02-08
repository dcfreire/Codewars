defmodule Twice do
  def start do
    Agent.start_link(fn -> %{0 => {%{0 => 1}, 0, 0}} end, name: __MODULE__)
  end

  def dbl_linear(n) do
    y = fn x -> 2 * x + 1 end
    z = fn x -> 3 * x + 1 end
    Twice.start()
    map = Agent.get(__MODULE__, fn map -> map end)
    IO.inspect(map)
    mapsize = map_size(map)
    IO.inspect(mapsize)

    Enum.reduce(
      (mapsize - 1)..(n - mapsize - 1),
      Agent.get(__MODULE__, &Map.get(&1, mapsize - 1)),
      fn x, acc ->
        yaux = y.(Map.get(elem(acc, 0), elem(acc, 1)))
        zaux = z.(Map.get(elem(acc, 0), elem(acc, 2)))

        cond do
          yaux <= zaux ->
            a = {Map.put(elem(acc, 0), x, yaux), elem(acc, 1) + 1, elem(acc, 2)}
            Agent.update(__MODULE__, &Map.put(&1, x, a))

            if yaux == zaux do
              a = {elem(acc, 0), elem(acc, 1), elem(acc, 2) + 1}
              Agent.update(__MODULE__, &Map.put(&1, x, a))
              a
            else
              acc
            end

          true ->
            a = {Map.put(elem(acc, 0), x, zaux), elem(acc, 1), elem(acc, 2) + 1}
            Agent.update(__MODULE__, &Map.put(&1, x, a))
            a
        end
      end
    )
    |> elem(0)
    |> Map.get(n)
  end
end
