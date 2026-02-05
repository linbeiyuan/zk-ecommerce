

<script setup lang="ts">
import { reactive } from 'vue';

const form = reactive({
  title: '',
  username: '',
  funddate: '',
  enddate: ''
});
</script>

<style scoped>
.add-edit-container {
  padding: 20px;
}
</style>
