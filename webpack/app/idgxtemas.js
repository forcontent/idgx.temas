import Contraste from './js/contrast.js';
import SocialLike from './js/sociallike';


$(() => {
  if ($('#viewlet-social-like')[0] != null) {
    new SocialLike();
  }
});

export default {
  Contraste,
  SocialLike,
}
