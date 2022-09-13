<template>
	<view class="image flex-row justify-center align-center">
		<image class="image" src="../../static/success.jpeg"></image>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		onShow() {
			this.jumpToForumTime()
		},
		methods: {
			jumpToForumTime() {
				setTimeout(() => {
					uni.redirectTo({
						url: 'forum',
					});
				}, 1000)
			},
		}
	}
</script>

<style>
	.image {
		display: flex;
		justify-content: center;
		align-content: center;
	}

	.content {
		width: 667rpx;
		height: 750tpx;
	}
</style>

