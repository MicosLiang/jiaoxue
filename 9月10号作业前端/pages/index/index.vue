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
					uni.request({
						url: 'http://127.0.0.1:8000/register/register',
						method: 'GET',
						data: {
							username: this.username,
							password: this.password
						},
						success: (res) => {
							if (res.data.status_code == 200) {
								this.title = '注册成功'
								uni.navigateTo({
									url: 'forum'
								});

							} else {
								uni.showModal({
									title: '注册失败'
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
									url: 'forum'
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
</style>

//
<!-- <template>
// 	<view class="content">
// 		<view style="margin-top: 200rpx;">
// 			<text class="title">{{title}}</text>
// 		</view>
// 		<view style="background-color:aquamarine;margin-top: 100rpx;">
// 			<input class="input" v-model="username" placeholder="用户名" />
// 			<view style="height: 30rpx;">

// 			</view>
// 			<input v-model="password" maxlength="16" placeholder="密码" />
// 		</view>
// 		<view style="margin-top: 100rpx;" class="button">
// 			<button @click="register">注册</button>
// 			<button @click="land">登录</button>
// 		</view>
// 	</view>
// 	</view>
// </template>

// <script>
// 	export default {
// 		data() {
// 			return {
// 				password: '',
// 				username: '',
// 				title: '欢迎来到9月10号作业'
// 			}
// 		},
// 		onLoad() {

// 		},
// 		methods: {
// 			register() {
// 				if (8 < password.length < 16) {
// 					uni.request({
// 						url: '',
// 						method: 'GET',
// 						data: {
// 							username: this.username,
// 							password: this.password
// 						},
// 						success: (res) => {
// 							if (res.data.status_code == 200) {
// 								this.title = '注册成功'
// 								uni.navigateTo({
// 									url: 'forum'
// 								});

// 							} else {
// 								uni.showModal({
// 									title: '注册失败'
// 								})
// 							}

// 						}
// 					})
// 				} else {
// 					uni.showToast({
// 						title: "请输入8到16位密码"

// 					})
// 				}
// 			},
// 			land() {
// 				uni.request({
// 					url: 'http://127.0.0.1:8000/main/login',
// 					method: 'GET',
// 					data: {
// 						username: this.username,
// 						password: this.password
// 					},
// 					success: (res) => {
// 						if (res.data.status_code == 200) {
// 							this.title = res.data.ans
// 							uni.navigateTo({
// 								url: 'forum'
// 							});

// 						} else {
// 							uni.showModal({
// 								title: res.data.ans
// 							})
// 						}
// 					}
// 				})
// 			}
// 		}
// 	}
// </script>

// <style>
// 	.content {
// 		display: flex;
// 		flex-direction: column;
// 		align-items: center;
// 		justify-content: start;
// 	}

// 	.logo {
// 		height: 200rpx;
// 		width: 200rpx;
// 		margin-top: 200rpx;
// 		margin-left: auto;
// 		margin-right: auto;
// 		margin-bottom: 50rpx;
// 	}

// 	.text-area {
// 		display: flex;
// 		justify-content: center;
// 	}

// 	.title {
// 		width: 156rpx;
// 		height: 37rpx;
// 		color: #1d770f;
// 		font-size: 26px;
// 		text-align: left;
// 		font-family: PingFangSC-bold;
// 		margin-top: 100rpx;
// 	}

// 	.buttonstyle {
// 		height: 10rpx;
// 		background-color: #FFFo;
// 		background-color: #8f8f94;
// 	}

// 	.input {
// 		display: flex;
// 		justify-content: start;
// 	}
// 	.button {
// 		width: 500rpx;
// 		display: flex;
// 		justify-content: space-between;
// 		}
// </style>
 // registerj() {
 // 	uni.navigateTo({
 // 		url:'land?username='  + this.username
 // 	})
 // },
 // register() {
 // 	uni.request({
 // 		url: 'http://127.0.0.1:8000/main/login',
 // 		method: 'GET',
 // 		data: {
 // 			username: this.username,
 // 			password: this.password
 // 		},
 // 		success: (res) => {
 // 			if (res.data.status_code == 200) {
 // 				this.title = res.data.ans
 // 				uni.navigateTo({
 // 					url: 'forum'
 // 				});
 
 // 			} else {
 // 				uni.showModal({
 // 					title: res.data.ans
 // 				})
 // 			}
 // 		},
 // 	})
