import { Category } from "./category";
import { Profile } from "./profile";
export class Post {
  id: any;
  constructor(
    public image: string,
    public video: File,
    public audio_track:File,
    public title: string,
    public category: Category,
    public article: string,
    public profile:Profile,
    public pub_at:Date,


    )
    {
    }

}