defmodule Factorial do
  def of(0), do: 1
  def of(n) when n > 0, do: n * of(n - 1)
end

# """
# defmodule Kata do
#  def to_factoradic(n) do
#    Enum.reduce_while(1..(n * n * n), {[], n}, fn x, acc ->
#      cond do
#        elem(acc, 1) == 0 ->
#          {:halt, acc}
#
#        true ->
#          {:cont, {[rem(elem(acc, 1), x) | elem(acc, 0)], div(elem(acc, 1), x)}}
#      end
#    end)
#    |> elem(0)
#  end
#
#  def permutation_by_number(word, n) do
#    word =
#      word
#      |> String.graphemes()
#      |> Enum.sort()
#
#    n =
#    n *
#      Enum.reduce(Enum.uniq(word), 1, fn char, acc ->
#        Enum.count(word, fn x ->
#          x == char
#        end)
#        |> Factorial.of()
#        |> (fn x -> x * acc end).()
#      end)
#
#    IO.inspect(n)
#
#    to_factoradic(n)
#    |> Enum.reduce({[], word}, fn x, acc ->
#      {[Enum.at(elem(acc, 1), x) | elem(acc, 0)], List.delete_at(elem(acc, 1), x)}
#    end)
#    |> elem(0)
#    |> Enum.reverse()
#    |> List.to_string()
#  end
# end
# """
ExUnit.start()

defmodule Kata do
  def permutation_by_number(word, n, current) when byte_size(word) == 0 do
    current
    |> Enum.reverse()
    |> List.to_string()
  end

  def permutation_by_number() do
    ""
  end

  def permutation_by_number(word, n, current \\ []) do
    freq =
      word
      |> String.graphemes()
      |> tl()
      |> Enum.uniq()
      |> (&Enum.reduce(&1, %{}, fn char, acc ->
            Enum.count(tl(String.graphemes(word)), fn x ->
              x == char
            end)
            |> (fn x -> Map.put(acc, char, x) end).()
          end)).()

    div(
      Factorial.of(Enum.sum(Map.values(freq))),
      Enum.reduce(freq, 1, fn x, acc ->
        Factorial.of(elem(x, 1)) * acc
      end)
    )
    |> (&(cond do
            &1 <= n ->
              String.graphemes(word)
              |> (fn y ->
                    List.pop_at(
                      y,
                      Enum.find_index(y, fn x -> x > hd(y) end)
                      |> (fn result ->
                            cond do
                              is_nil(result) ->
                                -1

                              true ->
                                result
                            end
                          end).()
                    )
                    |> (fn k ->
                          cond do
                            k < 0 -> [elem(k, 0) | elem(k, 1)]
                          end
                        end).()
                  end).()
              |> List.to_string()
              |> Kata.permutation_by_number(
                n - &1,
                current
              )

            &1 > n ->
              String.graphemes(word)
              |> List.pop_at(0)
              |> (fn x ->
                    Kata.permutation_by_number(List.to_string(Enum.sort(elem(x, 1))), n, [
                      elem(x, 0) | current
                    ])
                  end).()

            true ->
              nil
          end)).()
  end
end
