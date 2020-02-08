defmodule CodewarsTest do
  use ExUnit.Case
  doctest Codewars

  test "greets the world" do
    Kata.permutation_by_number("EEIRRRTW", 3060)
  end
end
