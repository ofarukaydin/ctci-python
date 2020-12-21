def weave(prefix, subtree5, subtree20, results):
    if not len(subtree5) or not len(subtree20):
        # One of the lists is empty, so join!
        results.append(prefix + subtree5 + subtree20)
        return results
    # Move leftmost item into prefix.
    head_subtree5 = subtree5.pop(0)
    prefix.append(head_subtree5)
    weave(prefix, subtree5, subtree20, results)
    # Return rightmost item to subtree5.
    prefix.pop()
    subtree5.insert(0, head_subtree5)
    # Move leftmost item into prefix.
    head_subtree20 = subtree20.pop(0)
    prefix.append(head_subtree20)
    weave(prefix, subtree5, subtree20, results)
    # Return rightmost item to subtree20.
    prefix.pop()
    subtree20.insert(0, head_subtree20)


results = []
weave([], [5, 2], [20, 30], results)
print(results)
