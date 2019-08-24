defmodule People do
  def list(people) do
    people =
      Enum.map(people, fn x -> Map.get(x, :name) end)
      |> Enum.filter(fn x -> String.length(x) > 0 end)
      |> Enum.intersperse(", ")

    people =
      Enum.map(0..(Enum.count(people) - 1), fn x ->
        cond do
          x == Enum.count(people) - 2 and Enum.at(people, x) == ", " ->
            " & "

          true ->
            Enum.at(people, x)
        end
      end)

    if Enum.at(people, 0) == nil do
      ""
    else
      List.to_string(people)
    end
  end
end
