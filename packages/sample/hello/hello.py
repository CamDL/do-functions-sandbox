def main(args):
      cat = args.get("cat", "all")
      payload = {'category':cat}
      #response = requests.get('https://inshortsapi.vercel.app/news',params=payload)
      return cat
  