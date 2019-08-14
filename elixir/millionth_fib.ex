defmodule Fib do
  use Agent

  def start do
    Agent.start_link(fn -> %{0 => 0, 1 => 1, -1 => 1, -2 => -1, 2 => 1} end, name: __MODULE__)
  end
  
  def  pow(n, k), do: pow(n, k, 1)
  defp pow(_, 0, acc), do: acc
  defp pow(n, k, acc), do: pow(n, k - 1, n * acc)

  def fib(n) do
    cached_value = Agent.get(__MODULE__, &(Map.get(&1, n)))
    if cached_value do
      cached_value
    else
     if rem(n, 2) == 1 do
      v = pow(fib(round(((n-1)/2))+1), 2) + pow(fib(round((n-1)/2)), 2)
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     else
      v = fib(round(n/2))*(2*fib(round((n)/2)+1) - fib(round(n/2)))
      Agent.update(__MODULE__, &(Map.put(&1, n, round(v))))
      round(v)
     end
    end
  end
end
