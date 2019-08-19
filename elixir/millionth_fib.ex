defmodule Fib do
  require Integer

  def start do
    Agent.start_link(fn -> %{0 => 0, 1 => 1, 2 => 1, -1 => 1} end, name: __MODULE__)
  end

  def pow(_, 0), do: 1
  def pow(x, n) when Integer.is_odd(n), do: x * pow(x, n - 1)
  def pow(x, n) do
    result = pow(x, div(n, 2))
    result * result
  end

  def fib_aux(n) do
    cached_value = Agent.get(__MODULE__, &(Map.get(&1, n)))
    if cached_value do
      cached_value
    else
     if rem(n, 2) == 1 do
      v = pow(fib_aux(round(((n-1)/2))+1), 2) + pow(fib_aux(round((n-1)/2)), 2)
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     else
      v = fib_aux(round(n/2))*(2*fib_aux(round((n)/2)+1) - fib_aux(round(n/2)))
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     end
    end
  end
  def fib(n) do
   Fib.start()
   if n < 0 and rem(n, 2) == 0 do
    fib_aux(n*(-1)) * (-1)
   else
    fib_aux(n)
   end
  end

end


# TODO: Replace examples and use TDD development by writing your own tests
defmodule MyFib do
  require Integer

  def start do
    Agent.start_link(fn -> %{0 => 0, 1 => 1, 2 => 1} end, name: __MODULE__)
  end

  def pow(_, 0), do: 1
  def pow(x, n) when Integer.is_odd(n), do: x * pow(x, n - 1)
  def pow(x, n) do
    result = pow(x, div(n, 2))
    result * result
  end

  def fib_aux(n) do
    cached_value = Agent.get(__MODULE__, &(Map.get(&1, n)))
    if cached_value do
      cached_value
    else
     if rem(n, 2) == 1 do
      v = pow(fib_aux(round(((n-1)/2))+1), 2) + pow(fib_aux(round((n-1)/2)), 2)
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     else
      v = fib_aux(round(n/2))*(2*fib_aux(round((n)/2)+1) - fib_aux(round(n/2)))
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     end
    end
  end
  def fib(n) do
   Fib.start()
   if n < 0 and rem(n, 2) == 0 do
    fib_aux(n*(-1)) * (-1)
   else
    fib_aux(n)
   end
  end

end

defmodule TestSolution do
  use ExUnit.Case

  test "Basic Tests" do
    assert Fib.fib(0) == 0
    assert Fib.fib(1) == 1
    assert Fib.fib(2) == 1
    assert Fib.fib(3) == 2
    assert Fib.fib(4) == 3
    assert Fib.fib(5) == 5
  end

defp testing(numtest, n, ans) do
  IO.puts("Test #{numtest} \n")
  assert Fib.fib(n) == ans
end

defp randomtests(n) when n <= 0 do
  IO.puts "Finished!"
end
defp randomtests(n, range) do
  u = Enum.random(range)
  ans = MyFib.fib(u)
  IO.puts("n #{u} \n --> solution : #{ans}")
  testing(n, u, ans)
  randomtests(n - 1)
end
test "Negative values" do
  :random.seed(:os.timestamp)
  assert Fib.fib(-6) == -8
  assert Fib.fib(-96) == -51680708854858323072
  randomtests(10, -100..-1)
end
test "Larger Values" do
  assert Fib.fib(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
  assert Fib.fib(1001) / Fib.fib(1000) == ((1 + :math.sqrt(5)) / 2)
  randomtests(1, 10000..100000)
  randomtests(1, 1000000..1500000)
end
end
