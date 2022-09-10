<template>
	<view class="content">
		<image class="logo" src="/static/logo.png"></image>
		<view class="text-area" style="display: flex;flex-direction: column;">
			<text class="title">{{title}}</text>
			<view style="background-color: #8f8f94;">
				<input v-model="chushu" placeholder="除数"/>
				<view style="height: 10rpx;background-color: #FFF;">
					
				</view>
				<input v-model="beichushu" placeholder="被除数"/>
			</view>
			<button @click="suan">submit</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				chushu : 1,
				beichushu : 1,
				title: ''
			}
		},
		onLoad() {

		},
		methods: {
			suan(){
				uni.request({
					url: 'http://127.0.0.1:8000/main/hello',
					method: 'GET',
					data: {
						n1 : this.chushu,
						n2 : this.beichushu
					},
					success: (res) => {
						if(res.data.status_code == 200){
							this.title = res.data.ans	
						}
						else{
							uni.showModal({
								title: res.data.ans
							})
						}
					},
					complete() {
						
					}
				})
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
