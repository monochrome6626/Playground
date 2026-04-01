import { SearchForm } from "@/components/search-form";
import { getLandmarks, getSpots } from "@/lib/api";

export default async function SearchPage() {
  const [spots, landmarks] = await Promise.all([getSpots(), getLandmarks()]);

  return <SearchForm spots={spots} landmarks={landmarks} />;
}
