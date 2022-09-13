<template>
	<view>
		<view class="content">
			<input v-model="text" placeholder="请输入一段文字吧~"/>
		</view>
		<view class="button-box">
			<button @click="submit">发条友善的帖子见证一下吧·</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text :'http://127.0.0.1:8000/post/createPost',
				username:''
			}
		},
		methods: {
			submit(){
				uni.request({
					url:'',
					method:'GET',
					data:{
						text : this.text
					},
				    success: (res) =>{
						if(res.data.status_code == 200){
							uni.navigateTo({
								url:"success"
							})
						}
					}
				})
				uni.navigateTo({
					url:'success'
				})
			}
		}
	}
</script>

<style>
	.content{
		margin: 30rpx 30rpx;
		height: 600rpx;
		font-weight: 675rpx;
		background-color: cornsilk;
		box-shadow: 1px 2px 9px 0px #d2d1d1;
		border-radius: 20rpx;
	}
</style>
