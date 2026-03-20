package count_special_triplets

func SpecialTriplets(nums []int) int {
	const mod = 1_000_000_007

	rightMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		rightMap[nums[i]]++
	}

	count := 0

	leftMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		rightMap[nums[i]]--

		if leftMap[nums[i]*2] > 0 && rightMap[nums[i]*2] > 0 {
			count = (count + leftMap[nums[i]*2]*rightMap[nums[i]*2]) % mod
		}

		leftMap[nums[i]]++
	}

	return count
}
