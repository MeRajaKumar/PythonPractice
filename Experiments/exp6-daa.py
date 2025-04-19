def find_subsets(S, target):
    result = []

    def backtrack(start, path, current_sum, mask):
        if current_sum == target:
            result.append((path[:], mask[:]))
            return
        if current_sum > target:
            return

        for i in range(start, len(S)):
            path.append(S[i])
            mask[i] = 1
            backtrack(i + 1, path, current_sum + S[i], mask)
            path.pop()
            mask[i] = 0

    backtrack(0, [], 0, [0]*len(S))

    if result:
        print("Subsets with sum", target, "are:")
        for subset, binary_mask in result:
            print("Subset:", subset, "→", binary_mask)
    else:
        print("No subset found with the given sum.")

