defmodule Divisible13 do

  def auxx(n) do
   rem = fn x ->
    cond do
     x == 1 ->
      10
     x == 10 ->
      9
     x == 9 ->
      12
     x == 12 ->
      3
     x == 3 ->
      4
     x == 4 ->
      1
     true ->
      1
    end
   end
   dig = Enum.reverse(Integer.digits(n))
   dr = Stream.iterate(1, rem)
   |> Enum.take(Enum.count(dig))
   Enum.map(0..Enum.count(dig)-1, fn x ->
     Enum.at(dig,x) * Enum.at(dr,x)
    end)
    |> Enum.sum()
  end

  def thirt(n) do
  Stream.unfold(n, fn i ->
   a = auxx(i)
   cond do
    i == a ->
     nil
    true ->
     {a, a}
   end
  end)
  |> Enum.to_list()
  |> Enum.reverse()
  |> Enum.at(0)
  end
end
