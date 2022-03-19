# Overview

![top](https://codejam.googleapis.com/dashboard/get_file/AQj_6U2TJsZ9UXhJfWvMM5G2u4j78N84faQu6TIWTXYEIRmnX69qtXjrlA/team.png)

This repo is for challenging HashCode 2022 by me, Takahira, Akima.

#HashCodeSolved
#HashCode-2022
#python

## challenging history
- 2022/2/25 7,402 points / 5075th (Thanks, Takahira-san!)
- 2022/3/10 branch: tananobo = 1,639,241 points

## explanation about tananobo branch

### how to use?
```
python main.py <[a-f(problem code)]>
```
### strategy

Anyway, I want to get plus score by coding (not manually). This is minimum function at start point.

1. create Contributor and Project class in input_reader.py
2. list of Projects are __randomly shuffled__
3. Iterate Projects using for loop
4. Check Projects required skills and Contributor skill one by one
5. If found, assign Contributor to each Project
6. __If not found, give up taking this Project__
7. __No mentor system or level up function are equipped at this code__

### learn from [hexmod](https://github.com/hexmod/hash-code-2022)

- Projectリストを式(ベストデイ-プロジェクト期間)が小さいものから順にsortしている。（ただしマイナスになるものは式の結果は9999999とする) [link](https://github.com/hexmod/hash-code-2022/blob/2cfa240fb56891f68b69af9619a1388938b5f138/src/main.py#L91)
- その後の処理はほぼ同じだが、Projectを受領できた場合にContributorをレベルアップさせている [link](https://github.com/hexmod/hash-code-2022/blob/2cfa240fb56891f68b69af9619a1388938b5f138/src/main.py#L109)
- 全てのタスクにContributorをアサインできなかった場合、Mentorを探すモードへ入る
- （コードが間違っている気はしますが[link](https://github.com/hexmod/hash-code-2022/blob/2cfa240fb56891f68b69af9619a1388938b5f138/src/Project.py#L19)[^1]）タスクがにContributorが割り当たっているか確認し、いない場合メンターの存在を確認
- メンターはこれまでに割り当てていた人の中から必要スキルをもっているかチェック
- メンターがいた場合は、一個レベル下のスキルの人を探す
- それでもプロジェクトが受けられない場合、仮アサインしていた人たちを解放
- メンター制度で割り当たった人のレベルアップ機能がないような

[^1]:return count in self.assignedRolesではなく,return role in self.assignedRolesでは？

### next to do for tananobo"2"
- [ ] sort Project list
- [ ] add level up Contributor
- [ ] add mentor system

## Reference Repo

https://github.com/mahmoudjobeel1/Google-HashCode-2022-Solutions (3,353,067point Java)

https://github.com/mhmd-azeez/google-hashcode-2022 (2,858,938 points C#)

https://github.com/hexmod/hash-code-2022 (2,539,814 points Python)

https://github.com/prague-pandas/hashcode-2022-qualification (score: 2,730,765 Python, Ruby)

## Japanese below

ここは私（棚瀬）と高比良さんと秋間さんがhashcode2022に挑戦するためのリポジトリです。

### hash code information

[hash code](https://codingcompetitions.withgoogle.com/hashcode/)

- チームは２〜４名で編成: [rib_lovers](https://codingcompetitions.withgoogle.com/hashcode/jointeam/00000000008caae7/00000000008fcb65/b59fda0d33f9e376)
- 初戦：Qualification Round 決戦:World Finals
- １位チーム賞金４千ドル（昨年）
- '21/11/22-22/2/17 Hub登録（オプショナル）
- '22/1/6-'2/13 個人登録
- '22/2/25(金) 日本時間2:30〜6:30 Qualification Round
- '22/3/3 結果発表
- 4/30 World Finals
- Hubとは？- Hash Code参加者組織のグループ(大学、会社単位）地方ごとなどで競い合ったり情報交換などするコミュニティ
- プログラミング言語、エディタは自由
- 競技時間中、ネット等情報源を見るのは良いが、チーム外の助けを借りるのはダメ
- 競技に参加するにはオンラインPFへログインが必要（詳細は後日）
- HPに過去問や練習問題などあり。チームを組んだ後MyTeamページから提出すると（練習問題は）採点してもらえる
