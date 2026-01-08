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
