defmodule Spin do
  def spin_words(message) do
    String.split(message, " ")
    |> Enum.map(fn x ->
      " " <>
        cond do
          String.length(x) > 4 ->
            String.reverse(x)

          true ->
            x
        end
    end)
    |> List.to_string()
    |> String.trim()
  end
end
