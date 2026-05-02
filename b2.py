import asyncio
import math
from datetime import datetime, timezone
from bilibili_api import video

async def main():
    v = video.Video(bvid="BV1aa4y1u7Ct")
    info = await v.get_info()
    
    # ========== 基础数据 ==========
    stat = info['stat']
    view = stat['view']
    like = stat['like']
    coin = stat['coin']
    favorite = stat['favorite']
    
    print(f"播放量: {view}")
    print(f"点赞数: {like}")
    print(f"投币数: {coin}")
    print(f"收藏数: {favorite}")
    
    # ========== 投稿日期 ==========
    pubdate_timestamp = info['pubdate']
    pubdate = datetime.fromtimestamp(pubdate_timestamp, tz=timezone.utc)
    pubdate_str = pubdate.strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n投稿日期: {pubdate_str}")
    
    # ========== 评分 ==========
    now = datetime.now(timezone.utc)
    days_since_pub = (now - pubdate).days
    
    t = math.log(days_since_pub / 14 + 1) + 1
    score = (like + coin * 2 + favorite * 2) * t
    
    print(f"\n投稿距今: {days_since_pub} 天")
    print(f"时间衰减因子 t: {t:.4f}")
    print(f"综合评分: {score:.2f}")

if __name__ == '__main__':
    asyncio.run(main())
