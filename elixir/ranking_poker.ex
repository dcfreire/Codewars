defmodule PokerHand do
  @result %{win: 1, loss: 2, tie: 3}
  @cards %{"T" => "10", "J" => "11", "Q" => "12", "K" => "13", "A" => "1", "D" => "0", "H" => "1", "C" => "2", "S" => "3"}


  def parse_hand(player) do
   player = Enum.chunk(Enum.filter(String.codepoints(player), fn x -> x != " " end), 2)
   |> Enum.map(fn [a, b] -> {Map.get(@cards, a, a), Map.get(@cards, b, b)} end)
   player =  Enum.map(0..Enum.count(player) -1, fn x ->
    {Enum.at(player, x), Enum.count(player, fn k -> elem(k, 0) == elem(Enum.at(player, x), 0) end)} end)
   |> Enum.sort_by(&(elem(elem(&1, 0), 0)))

  end


  def eval_hand(player) do
   Enum.count(player, fn x ->
    elem(elem(x, 0), 1) == elem(elem(Enum.at(player, 0), 0), 1)
   end)
   Enum.reduce(player, {0, ""}, fn x, acc->
    cond do
     elem(acc, 0) == 0 ->
      {1, elem(elem(x, 0), 0)}
      String.to_integer(elem(elem(x, 0), 0)) == String.to_integer(elem(acc, 1)) ->
       {elem(acc, 0) + 1, elem(elem(x, 0), 0)}
       true ->
         {-1, ""}
    end
   end)
  end


  def compare(player, opponent) do
   parse_hand(player)

  end

end
