BFS(Graph, Start)
    Visited ← empty set
    Queue ← empty queue

    add Start to Queue
    add Start to Visited

    while Queue not empty do
        Node ← dequeue Queue
        print Node

        for each Neighbor in Graph[Node] do
            if Neighbor not in Visited then
                add Neighbor to Visited
                enqueue Neighbor
            end if
        end for
    end while
END




DFS(Graph, Node, Visited)
    add Node to Visited
    print Node

    for each Neighbor in Graph[Node] do
        if Neighbor not in Visited then
            DFS(Graph, Neighbor, Visited)
        end if
    end for
END




UCS(Graph, Start, Goal)
    PriorityQueue ← (0, Start, [Start])
    Visited ← empty set

    while PriorityQueue not empty do
        (Cost, Node, Path) ← pop minimum

        if Node = Goal then
            return Path, Cost
        end if

        if Node not in Visited then
            add Node to Visited

            for each (Neighbor, EdgeCost) in Graph[Node] do
                push (Cost + EdgeCost, Neighbor, Path + Neighbor)
            end for
        end if
    end while
END
