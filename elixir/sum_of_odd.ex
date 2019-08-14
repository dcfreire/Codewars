defmodule SumOfOdd do
  def row_sum_odd_numbers(n) do
    Enum.map(div((n*(n+1)),2) - n + 1..div(n*(n+1),2), fn x -> 2*x - 1 end)
    |> Enum.sum()
  end
end


### TEST CASES ###

# TODO: Replace examples and use TDD development by writing your own tests
defmodule Sum do
  def sum(n) do
    Enum.map(div((n*(n+1)),2) - n + 1..div(n*(n+1),2), fn x -> 2*x - 1 end)
    |> Enum.sum()
  end
end

defmodule TestSolution do
  use ExUnit.Case

  test "Basic Tests" do
    assert SumOfOdd.row_sum_odd_numbers(1) == 1
    assert SumOfOdd.row_sum_odd_numbers(2) == 8
    assert SumOfOdd.row_sum_odd_numbers(13) == 2197
    assert SumOfOdd.row_sum_odd_numbers(19) == 6859
    assert SumOfOdd.row_sum_odd_numbers(41) == 68921
    assert SumOfOdd.row_sum_odd_numbers(42) == 74088
    assert SumOfOdd.row_sum_odd_numbers(74) == 405224
    assert SumOfOdd.row_sum_odd_numbers(86) == 636056
    assert SumOfOdd.row_sum_odd_numbers(93) == 804357
    assert SumOfOdd.row_sum_odd_numbers(101) == 1030301
  end

defp testing(numtest, n, ans) do
  IO.puts("Test #{numtest} \n")
  assert SumOfOdd.row_sum_odd_numbers(n) == ans
end

defp randomtests(n) when n <= 0 do
  IO.puts "Finished!"
end
defp randomtests(n) do
  u = :random.uniform(500)
  ans = Sum.sum(u)
  IO.puts("n #{u} \n --> solution : #{ans}")
  testing(n, u, ans)
  randomtests(n - 1)
end
test "Random tests" do
  :random.seed(:os.timestamp)
  randomtests(50)
end

end
