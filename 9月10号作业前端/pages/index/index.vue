<template>
	<view class="content justify-center">
		<view class="text">
			<b>用户名密码登录</b>
		</view>
		<view class="information flex-column">
			<input v-model="username" class="usernamebox" placeholder="账号:" />
			<input v-model="password" class="passwordbox" placeholder="密码:" />
			<button @click="register()" class="buttonbox">注册</button>
			<button @click="login()" class="buttonbox">登录</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				username: '',
				password: '',
			}
		},
		onLoad() {

		},
		methods: {
			register() {
				if (8 <= this.password.length & this.password.length <= 16) {
					let that = this
					uni.request({
						url: 'http://127.0.0.1:8000/register/register',
						method: 'GET',
						data: {
							username: that.username,
							password: that.password
						},
						success: (res) => {
							if (res.data.status_code == 200) {
								that.title = '注册成功'
								uni.navigateTo({
									url: 'forum?username='+that.username
								});

							} else {
								uni.showModal({
									title: '注册失败,用户名已存在'
								})
							}

						}
					})
				} else {
					uni.showToast({
						title: "请输入8到16位密码"

					})
				}
			},
			login() {
				let that=this
				uni.request({
						url: 'http://127.0.0.1:8000/login/login',
						method: 'GET',
						data: {
							username: this.username,
							password: this.password
						},
						
						
						success: (res) => {
							if (res.data.status_code == 200) {
								this.title = res.data.ans
								uni.navigateTo({
									url: 'forum?username='+that.username
								});

							} else {
								uni.showModal({
									title: res.data.ans
								})
							}
						}




					})
				},
			},
	}
</script>
<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		width: 100vw;
	}

	.buttonbox {
		height: 50px;
		width: 200px;
		margin: 10px;
	}
	.text {
		font-weight: 700;
		font-size: 50rpx;
		margin:60rpx;
		
	}
	.function {
		
	}

	.usernamebox {
		margin:10rpx;
		background-color: antiquewhite;
		padding: 20rpx;
		border-radius: 20rpx;
	}
	
	.passwordbox {
		margin:10rpx;
		background-color: antiquewhite;
		padding: 20rpx;
		border-radius: 20rpx;
	}
	.information {
		display: flex;
		justify-content: center;
	}
	
</style>

<!-- <style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		width: 100vw;
	}

	.buttonbox {
		height: 50px;
		width: 200px;
		margin: 10px;
	}

	.text {
		font-weight: 700;
		font-size: 50rpx;
		margin: 60rpx;

	}

	.usernamebox {
		margin: 10rpx;
		background-color: antiquewhite;
		padding: 20rpx;
		border-radius: 20rpx;
	}

	.passwordbox {
		margin: 10rpx;
		background-color: antiquewhite;
		padding: 20rpx;
		border-radius: 20rpx;
	}

	.information {
		display: flex;
		justify-content: center;
	}
</style> -->
