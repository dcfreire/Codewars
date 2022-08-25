defmodule CodewarsTest do
  use ExUnit.Case
  doctest Codewars

  test "greets the world" do
    a = Kata.permutation_by_number("NMOIM", 44)
    IO.inspect(a)
  end
end
