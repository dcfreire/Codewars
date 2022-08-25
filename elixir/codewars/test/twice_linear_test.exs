defmodule TwiceTest do
  use ExUnit.Case
  doctest Twice

  def dotest(n, exp) do
    IO.puts("Testing : #{n}")
    act = Twice.dbl_linear(n)
    IO.puts("act: #{act}")
    IO.puts("exp: #{exp}")
    assert act == exp
    IO.puts("#")
  end

  test "dbl_linear" do
    dotest(10, 22)
    dotest(20, 57)
    dotest(30, 91)
    dotest(50, 175)
  end
end
