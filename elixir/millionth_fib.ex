defmodule Fib do
  use Agent
  require Integer

  def start do
    Agent.start_link(fn -> %{0 => 0, 1 => 1, -1 => 1, -2 => -1, 2 => 1} end, name: __MODULE__)
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
