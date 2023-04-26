
import networkx as nx
from transformers import AutoModel, AutoTokenizer

temp_path = input("请输入模型地址")
input("按下回车键后开始加载模型...")

tokenizer = AutoTokenizer.from_pretrained("C:\AIproject\ChatGLM-6B\model\chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("C:\AIproject\ChatGLM-6B\model\chatglm-6b-int4", trust_remote_code=True).half().cuda()
model = model.eval()

input("按下回车键后开始测试模型...")

prompt = "写一份关于自由的信"
def chatGLM_generate(prompt,max_length):
    input = prompt
    for response, chat_history in model.stream_chat(tokenizer, input, history=None,max_length=max_length, top_p=0.7, temperature=1):
        response = chat_history[-1]
    return response
out_text=chatGLM_generate(prompt, max_length=128)

print(out_text)

import networkx as nx
prompt = "steam是什么？"
def generate(generate_prompt,generatemax_length):
  out = chatGLM_generate(prompt=generate_prompt,max_length=generatemax_length)
  return out[1]
print(generate(prompt,128))


# ## 世界描述
# 
# 我们描述下面的世界。我们将根据这些信息生成提示。模拟的是无冬城西南的Phandalin镇。之所以选择这个区域，是因为它很容易扩展成多个区域，让“玩家”能够在模拟完成后探索世界。

world_graph = nx.Graph()
prompt_meta = "{}"
town_areas = ["巴瑟恩杂货店", "狮盾贸易公司", "斯通希尔旅店", "芬达林镇广场"]
town_areas = {
"芬达林镇广场": "芬达林镇的市中心广场。",
"石山客栈": "镇中心有一座由石块和粗糙板材建成的大型路边店。公共休息室里坐着当地人，他们抱着麦酒或苹果酒，都好奇地盯着你看。",
"巴瑟恩的货栈": "芬达林最大的贸易站是巴瑟恩的货栈。货架上摆满了大部分普通物品和用品，包括背包、棉被、绳索和口粮。这个地方从日出到日落都开放。",
"艾德玛斯果园": "一个整洁的小木屋旁边的苹果园。",
"狮盾集团": "这家不起眼的交易站前门上悬挂着一个木制盾牌形状的招牌，上面画着一头蓝色的狮子。这座建筑由狮盾公司所拥有，该公司总部位于东面100多英里的亚塔市。他们向芬达林和其他小定居点运送成品，但这个前哨站受到了强盗的严重打击。最近应该会到达芬达林的狮盾商队没有出现。",
"芬达林矿工交易所": "矿工交易所是当地矿工把他们有价值的发现放在那里称重、测量并支付报酬的贸易站。在缺乏任何本地领主或权威的情况下，该交易所还充当非官方的记录办公室，在该区域注册各种流和开挖权利。芬达林没有真正的淘金热，但足够的财富隐藏在附近的小溪和山谷中，可以支持相当数量的独立探矿者。该交易所是一个很好的地方，可以结识到经常在芬达林周围的乡村活动的人。会长是一位名叫哈利亚·桑德尔顿的野心勃勃、精明计算的人类女性。",
"奥德利芙农场": "由乐于助人的半身人农民奎琳·奥德利芙拥有的农场。",
"幸运神殿": "芬达林唯一的寺庙，这是一个由附近废墟中取来的石头建成的小神殿。它致力于侍奉提摩拉女神——幸运和好运女神。",
"沉睡巨人": "这个破旧的酒馆位于芬达林主街尽头，是一个肮脏、危险的水源。红袍暴徒经常光顾，由妮莉·星匠经营。",
"镇长大厅": "镇长大厅有坚固的石墙、倾斜的木屋顶和后面的钟楼。在前门旁边的一块板子上张贴着一则用通用语写成的告示。上面写着：“悬赏通告——温沃恩山区附近有兽人！那些有勇气直面兽人威胁的人应该来这里打听打听。”这则告示上印有小镇的印章和无法辨认的签名。",
"特雷森达庄园": "红袍暴徒团伙在芬达林的基地是位于特雷森达庄园的地下室。在这个庄园被废弃之前，它的地下室被用作存储食物和水的安全场所以备战不测，同时相邻的墓穴为特雷森达家族已故成员提供了一个安息之所。自从红袍暴徒团伙接管后，他们已经扩建了地下室，加入了奴隶囚笼、车间和营房等设施来满足他们自己的目的。"
}
town_people = {
"托布伦·斯通希尔": "托布伦拥有一家贸易站。",
"达兰·艾德玛斯": "达兰是一位退役冒险家，住在一个整洁的小木屋旁边的苹果园里。他是一位身材健壮、银发半精灵，已经过百岁的战士，在东南方的龙海岸领地中担任元帅和传令官多年。退役后，他回到了他的故乡——尼瓦伦地区。",
"莱宁·格雷温德": "莱宁经营着一家贸易站。",
"哈莉亚·桑顿": "哈莉亚是一个野心勃勃、精明计算的人类女性。她是芬达林矿工交易所的行会大师，该贸易站称重、测量并支付当地矿工有价值的发现。为了将矿工交易所建立成城镇最接近治理权力的事物，她不止是一个简单的商人。",
"奎琳·奥德利芙": "奎琳是一位45岁充满智慧的矮人农民，似乎知道镇上发生的一切。她是友善的人，如果他们不想住在巴瑟恩的货栈，愿意让流浪者留在她的干草棚里。",
"盖蕾尔修女": "盖蕾尔修女是提摩拉的精灵神职人员。",
"哈宾·韦斯特": "哈宾是芬达林镇长。一个自命不凡、年迈的食品商。芬达林没有政府，但镇民每年选出一个人来担任镇长。镇长在一些小的纠纷中担任法官，并保管需要保管的任何记录。",
"泰瑞尔·血痕": "泰瑞尔是一个人类恶棍。他穿着肮脏的绯红色斗篷，并且是红袍暴徒的成员。他不喜欢冒险家，想抢劫和杀死冒险家。",
"妮莉·星匠": "妮莉是一个人类恶霸。她穿着肮脏的绯红色斗篷，并且是红袍暴徒的成员。她不喜欢冒险家，想抢劫和杀死冒险家。",
}
for town_area in town_areas.keys():
  world_graph.add_node(town_area)
  world_graph.add_edge(town_area, town_area)
for town_area in town_areas.keys():
  world_graph.add_edge(town_area, "芬达林镇广场")
locations = {}
for i in town_people.keys():
  locations[i] = "芬达林镇广场"
memories = {}
for i in town_people.keys():
  memories[i] = []
plans = {}
for i in town_people.keys():
  plans[i] = []

global_time = 8
def generate_description_of_area(x):
  text = "现在是 "+str(global_time)+":00. 地点是 "+x+"."
  people = []
  for i in locations.keys():
    if locations[i] == x:
      people.append(i)
compressed_memories_all = {}
for name in town_people.keys():
  compressed_memories_all[name] = []


input("按下回车键后开始生成目标...")

for name in town_people.keys():
  prompt = "你是 {}。{} 你刚在芬达林镇广场醒来然后去了镇广场。下面的人住在镇上: {}。你今天的目标是什么？从你的角度回答，最多用30个字来描述".format(name, town_people[name], ', '.join(list(town_people.keys())) )
  plans[name] = generate(prompt_meta.format(prompt),len(prompt_meta.format(prompt))+128)
  print(name, plans[name])

action_prompts = {}
for location in town_areas.keys():
  people = []
  for i in town_people.keys():
    if locations[i] == location:
      people.append(i)
  
  for name in people:
    prompt = "你是 {}. {} 你计划去做: {}. 你目前在 {} 其描述如下: {}. 当前时间为 {}:00. 这个区域里有以下人员: {}. 你可以与他们进行互动。".format(name, town_people[name], plans[name], location, town_areas[location], str(global_time), ', '.join(people))
    people_description = []
    for i in people:
      people_description.append(i+': '+town_people[i])
    prompt += ' 你知道以下人员的信息: ' + '. '.join(people_description)
    memory_text = '. '.join(memories[name][-10:])
    prompt += "接下来的一个小时你要做什么?最多用20个字来描述。"
    action_prompts[name] = prompt

action_results = {}
for name in town_people.keys():
  action_results[name] = generate(prompt_meta.format(action_prompts[name]),len(prompt_meta.format(action_prompts[name])))
  # Now clean the action
  prompt = """
  将以下段落转换为第一人称过去式:
  "{}"
  """.format(action_results[name])
  action_results[name] = generate(prompt_meta.format(prompt),len(prompt_meta.format(prompt))).replace('"', '').replace("'", '')
  print(name, action_results[name])


input("按下回车键后开始收集记忆...")
# 收集人们观察到的记忆。
action_prompts = {}
for location in town_areas.keys():
  people = []
  for i in town_people.keys():
    if locations[i] == location:
      people.append(i)
  
  for name in people:
    for name_two in people:
      memories[name].append('[时间: {}. 人物: {}. 记忆: {}]\n'.format(str(global_time), name_two, action_results[name_two]))


# 记忆排序

import re
def get_rating(x):
  nums = [int(i) for i in re.findall(r'\d+', x)]
  if len(nums)>0:
    return min(nums)
  else:
    return None
memory_ratings = {}
for name in town_people.keys():
  memory_ratings[name] = []
  for i, memory in enumerate(memories[name]):
    prompt = "你是 {}. 你计划: {}. 你目前在 {}. 当前时间为 {}:00. 你可以观察到以下内容: {}. 将你对于这件事关心的程度评为1到5分。".format(name, plans[name], locations[name], str(global_time), memory)
    res = generate(prompt_meta.format(prompt),len(prompt_meta.format(prompt)))
    rating = get_rating(res)
    max_attempts = 2
    current_attempt = 0
    while rating is None and current_attempt<max_attempts:
      rating = get_rating(res)
      current_attempt += 1
    if rating is None:
      rating = 0
    memory_ratings[name].append((res, rating))
  print(memory_ratings[name])

input("按下回车键后开始压缩记忆...")
# # 压缩记忆

MEMORY_LIMIT = 10
compressed_memories = {}
for name in town_people.keys():
  memories_sorted = sorted(
        memory_ratings[name], 
        key=lambda x: x[1]
    )[::-1]
  relevant_memories = memories_sorted[:MEMORY_LIMIT]
  # print(name, relevant_memories)
  memory_string_to_compress = '.'.join([a[0] for a in relevant_memories])
  prompt = "你是 {}. 你的计划是: {}. 你目前在 {}. 当前时间为 {}:00. 你可以观察到以下内容: {}. 用一句话概括这些记忆。".format(name, plans[name], locations[name], str(global_time), memory_string_to_compress)
  res = generate(prompt_meta.format(prompt),len(prompt_meta.format(prompt)))
  compressed_memories[name] = '[在 {}:00 的回忆: {}]'.format(str(global_time), res)
  compressed_memories_all[name].append(compressed_memories[name])

place_ratings = {}
for name in town_people.keys():
  place_ratings[name] = []
  for area in town_areas.keys():
    prompt = "你是 {}. 你的计划是: {}. 你目前在 {}. 当前时间为 {}:00. 你有以下记忆: {}. 请给出一个1到5之间的评分,用于表示你在接下来的一个小时内有多大可能会去 {}".format(name, plans[name], locations[name], str(global_time), compressed_memories[name], area)
    res = generate(prompt_meta.format(prompt))
    rating = get_rating(res)
    max_attempts = 2
    current_attempt = 0
    while rating is None and current_attempt<max_attempts:
      rating = get_rating(res)
      current_attempt += 1
    if rating is None:
      rating = 0
    place_ratings[name].append((area, rating, res))
  place_ratings_sorted = sorted(
      place_ratings[name], 
      key=lambda x: x[1]
  )[::-1]
  if place_ratings_sorted[0][0] != locations[name]:
    new_recollection = '[在 {}:00 的回忆: {}]'.format(str(global_time), '然后我搬到了 {}.'.format(place_ratings_sorted[0][0]))
    compressed_memories_all[name].append(new_recollection)
  locations[name] = place_ratings_sorted[0][0]


input("按下回车键后开始循环执行5次(这将会花费很多时间)...")
# # 程序汇总

for repeats in range(5):
  global_time += 1
  action_prompts = {}
  for location in town_areas.keys():
    people = []
    for i in town_people.keys():
      if locations[i] == location:
        people.append(i)
    
    for name in people:
      prompt = "你是 {}. 你的计划是: {}. 你目前在 {} 其描述如下: {}. 你的记忆是: {}. 当前时间为 {}:00. 这个区域里有以下人员: {}. 你可以与他们进行互动。".format(name, plans[name], location, town_areas[location], '\n'.join(compressed_memories_all[name][-5:]), str(global_time), ', '.join(people))
      people_description = []
      for i in people:
        people_description.append(i+': '+town_people[i])
      prompt += ' 你知道以下人员的信息: ' + '. '.join(people_description)
      memory_text = '. '.join(memories[name][-10:])
      prompt += "接下来的一个小时你要做什么?最多用20个字来描述。"
      action_prompts[name] = prompt
  action_results = {}
  for name in town_people.keys():
    action_results[name] = generate(prompt_meta.format(action_prompts[name]))
    # Now clean the action
    prompt = """
    将以下段落转换为第一人称过去式:
    "{}"
    """.format(action_results[name])
    action_results[name] = generate(prompt_meta.format(prompt)).replace('"', '').replace("'", '')
    print(name, locations[name], global_time, action_results[name])
  action_emojis = {}
  for name in town_people.keys():
    prompt = """
    将下面的段落转换为tuple (Action, Object):
    "{}"
    """.format(action_results[name])
    action_emojis[name] = generate(prompt_meta.format(prompt)).replace('"', '').replace("'", '')
    print('    - Emoji 表示:', name, locations[name], global_time, action_emojis[name])
  action_prompts = {}
  for location in town_areas.keys():
    people = []
    for i in town_people.keys():
      if locations[i] == location:
        people.append(i)
    
    for name in people:
      for name_two in people:
        memories[name].append('[时间: {}. 人物: {}. 记忆: {}]\n'.format(str(global_time), name_two, action_results[name_two]))

  memory_ratings = {}
  for name in town_people.keys():
    memory_ratings[name] = []
    for i, memory in enumerate(memories[name]):
      prompt = "你是 {}. 你的计划是: {}. 你的记忆是: {}. 你目前在 {}. 当前时间为 {}:00. 这个区域里有以下人员: {}. 将你对于这件事关心的程度评为1到5分。".format(name, plans[name], '\n'.join(compressed_memories_all[name][-5:]), locations[name], str(global_time), memory)
      res = generate(prompt_meta.format(prompt))
      rating = get_rating(res)
      max_attempts = 2
      current_attempt = 0
      while rating is None and current_attempt<max_attempts:
        rating = get_rating(res)
        current_attempt += 1
      if rating is None:
        rating = 0
      memory_ratings[name].append((res, rating))

  compressed_memories = {}
  for name in town_people.keys():
    memories_sorted = sorted(
          memory_ratings[name], 
          key=lambda x: x[1]
      )[::-1]
    relevant_memories = memories_sorted[:MEMORY_LIMIT]
    memory_string_to_compress = '.'.join([a[0] for a in relevant_memories])
    prompt = "你是 {}. 你的计划是: {}. 你目前在 {}. 当前时间为 {}:00. 你可以观察到以下内容: {}. 用一句话概括这些记忆。".format(name, plans[name], locations[name], str(global_time), memory_string_to_compress)
    res = generate(prompt_meta.format(prompt))
    compressed_memories[name] = '[在 {}:00 的回忆: {}]'.format(str(global_time), res)
    compressed_memories_all[name].append(compressed_memories[name])

  place_ratings = {}

  for name in town_people.keys():
    place_ratings[name] = []
    for area in town_areas.keys():
      prompt = "你是 {}. 你的计划是: {}. 你目前在 {}. 当前时间为 {}:00. 你有以下记忆: {}. 请给出一个1到5之间的评分,用于表示你在接下来的一个小时内有多大可能会去 {}。".format(name, plans[name], locations[name], str(global_time), compressed_memories[name], area)
      res = generate(prompt_meta.format(prompt))
      rating = get_rating(res)
      max_attempts = 2
      current_attempt = 0
      while rating is None and current_attempt<max_attempts:
        rating = get_rating(res)
        current_attempt += 1
      if rating is None:
        rating = 0
      place_ratings[name].append((area, rating, res))
    place_ratings_sorted = sorted(
        place_ratings[name], 
        key=lambda x: x[1] )[::-1]
    if place_ratings_sorted[0][0] != locations[name]:
      new_recollection = '[在 {}:00 的回忆: {}]'.format(str(global_time), '然后我搬到了 {}.'.format(place_ratings_sorted[0][0]))
      compressed_memories_all[name].append(new_recollection)
    locations[name] = place_ratings_sorted[0][0]


out_path = input("请输入导出数据的目录(例如D:/generatedtext):")
input("按下回车键后开始导出各项数据...")

import json
with open(out_path+'/计划.json', 'w',encoding='utf-8') as f:
    json.dump(plans, f, ensure_ascii=False)
with open(out_path+'位置.json', 'w',encoding='utf-8') as f:
    json.dump(location, f, ensure_ascii=False)
with open(out_path+'记忆.json', 'w',encoding='utf-8') as f:
    json.dump(memories,f, ensure_ascii=False)
with open(out_path+'所有压缩记忆.json', 'w',encoding='utf-8') as f:
    json.dump(compressed_memories_all, f, ensure_ascii=False)
with open(out_path+'记忆评分.json', 'w',encoding='utf-8') as f:
    json.dump(people, f, ensure_ascii=False)

