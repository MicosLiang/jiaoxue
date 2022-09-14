<template>
	<view class="image flex-row justify-center align-center">
		<image class="image" src="../../static/success.jpeg"></image>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				username:''
			}
		},
		onLoad(res) {
			this.username=res.username
		},
		onShow() {
			this.jumpToForumTime()
		},
		methods: {
			jumpToForumTime() {
				let that=this
				setTimeout(() => {
					uni.redirectTo({
						url: 'forum?username='+that.username,
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

