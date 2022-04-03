import { Post } from "./post";
import { Profile } from "./profile";

export class Wishlist {
  constructor(
    public post: Post,
    public profile: Profile,

  )
  {

  }
}