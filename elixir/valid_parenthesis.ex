defmodule ParenthesesValidator do
  def valid_parentheses(string) do
    a = Enum.reduce(String.codepoints(string), 0, fn x, acc ->
     cond do
      acc < 0 ->
       acc
      x == "(" ->
       acc + 1
      x == ")" ->
       acc - 1
      true ->
       acc
      end
     end)
    cond do
     a == 0 ->
      true
     true ->
      false
    end
  end
end
