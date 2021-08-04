defmodule Twice do
  def start do
    try do
      :ets.new(__MODULE__, [:named_table, :public])
      :ets.insert(__MODULE__, {0, {1, 0, 0}})
    rescue
      _ ->
        :already_exists
    end
  end

  defp lookup(key) do
    :ets.lookup_element(__MODULE__, key, 2)
  end

  def dbl_linear(n) do
    y = fn x -> 2 * x + 1 end
    z = fn x -> 3 * x + 1 end
    Twice.start()
    mapsize = :ets.info(__MODULE__)[:size]

    if mapsize < n do
      Enum.reduce(
        mapsize..n,
        :ets.lookup_element(__MODULE__, mapsize - 1, 2),
        fn x, acc ->

          yaux =
            elem(acc, 1)
            |> lookup()
            |> elem(0)
            |> y.()

          zaux =
            elem(acc, 2)
            |> lookup()
            |> elem(0)
            |> z.()

          cond do
            yaux <= zaux ->
              a = {yaux, elem(acc, 1) + 1, elem(acc, 2)}
              :ets.insert(__MODULE__, {x, a})

              if yaux == zaux do
                a = {yaux, elem(acc, 1) + 1, elem(acc, 2) + 1}
                :ets.insert(__MODULE__, {x, a})
                a
              else
                a
              end

            true ->
              a = {zaux, elem(acc, 1), elem(acc, 2) + 1}
              :ets.insert(__MODULE__, {x, a})
              a
          end
        end
      )
      |> elem(0)
    else
      :ets.lookup_element(__MODULE__, n, 2)
      |> elem(0)
    end
  end
end
